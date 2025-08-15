# Sync template updates into your site

**Repos**

- Template: `khan-lab/seminar-website-template`
- Example Website: `khan-lab/ilm-seminars`

This short guide shows how to merge changes from the template into your site, plus an optional automation so future updates arrive as PRs.

---

## One-time merge (manual)

1. **Create a working branch in the site repo**

   ```bash
   git clone git@github.com:khan-lab/ilm-seminars.git
   cd ilm-seminars
   git checkout -b sync-template-$(date +%Y%m%d)
   ```

2. **Add the template as a remote and fetch**

   ```bash
   git remote add template https://github.com/khan-lab/seminar-website-template.git
   git fetch template
   ```

3. **(Optional) Protect site-specific files during merges** Add a merge driver and a `.gitattributes` so your local versions win when merging:

   ```bash
   git config merge.ours.driver true
   cat > .gitattributes <<'EOF'
   # Keep these from the site when merging the template
   _config.yml        merge=ours
   CNAME              merge=ours
   _data/**           merge=ours
   assets/uploads/**  merge=ours
   speakers.yml       merge=ours
   EOF
   git add .gitattributes
   git commit -m "chore: prefer site files on template merges"
   ```

4. **Merge the template’s default branch** (change `main` if needed):

   ```bash
   git merge template/main --no-ff --allow-unrelated-histories
   ```

5. **Resolve conflicts**

   - Keep the site’s version of a file: `git checkout --ours path/to/file`
   - Take the template’s version: `git checkout --theirs path/to/file`
   - After resolving: `git add -A && git commit`

6. **Test locally**

   ```bash
   bundle install
   bundle exec jekyll serve
   ```

7. **Push and open a PR**

   ```bash
   git push -u origin HEAD
   ```

   Review the diff in GitHub and merge to your main branch when satisfied.

> Tip: Repeat steps 2, 4–7 whenever you want to bring in the latest template updates.

---

## Automate future updates (recommended)

Set up a GitHub Action in `ilm-seminars` that periodically pulls changes from the template and opens a PR.

1. **Add **`` at the repo root to skip site-specific paths:

   ```gitignore
   # keep site-specific config and data
   _config.yml
   CNAME
   _data/**
   assets/uploads/**
   speakers.yml
   ```

2. **Create workflow** at `.github/workflows/template-sync.yml`:

   ```yaml
   name: Sync from template
   on:
     schedule:
       - cron: "0 3 * * 1" # every Monday 03:00 UTC
     workflow_dispatch: {}
   jobs:
     sync:
       runs-on: ubuntu-latest
       permissions:
         contents: write
         pull-requests: write
       steps:
         - uses: actions/checkout@v4
         - uses: AndreasAugustin/actions-template-sync@v2
           with:
             source_repo_path: khan-lab/seminar-website-template
             upstream_branch: main
             pr_labels: template-sync
             # optional if you rename the ignore file:
             # template_sync_ignore_file_path: .github/my-sync-ignore
   ```

The action will open a PR whenever there are changes in the template, honoring `.templatesyncignore`.

---

### Quick commands reference

```bash
# Add template remote once
git remote add template https://github.com/khan-lab/seminar-website-template.git

# Bring latest template changes and merge
git fetch template
git merge template/main --no-ff --allow-unrelated-histories

# Resolve conflicts quickly
git checkout --ours path/to/file   # keep site version
git checkout --theirs path/to/file # take template version
```
