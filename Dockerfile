FROM ruby:3.2-slim

# Install build deps + Python + PyYAML
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    build-essential git ca-certificates python3 python3-yaml \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Install gems globally so bind mounts don't hide them
ENV BUNDLE_PATH=/usr/local/bundle

# Install gems first (better caching)
COPY Gemfile Gemfile.lock* ./

# Add all the platforms you want supported
RUN bundle lock \
    --add-platform ruby \
    --add-platform x86_64-linux \
    --add-platform x86_64-linux-musl \
    --add-platform aarch64-linux \
    --add-platform aarch64-linux-gnu \
    --add-platform arm64-darwin \
    --add-platform x86_64-darwin

RUN bundle install --jobs 4 --retry 3

# Copy the rest (including scripts/)
COPY . .

EXPOSE 4000

ENTRYPOINT ["./start.sh"]
