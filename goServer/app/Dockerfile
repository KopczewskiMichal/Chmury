
# Build Stage

FROM golang:1.22.0-alpine AS BuildStage

WORKDIR /crud


COPY . .

RUN go mod download


EXPOSE 3000

RUN go build -o /test main.go

# Deploy Stage

FROM alpine:latest

WORKDIR /

COPY attacks.json attacks.json
COPY --from=BuildStage /test /test

EXPOSE 3000

# USER nonroot:nonroot

ENTRYPOINT ["/test"]


