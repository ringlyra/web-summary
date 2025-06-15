---
title: What web frameworks does Firebase App Hosting support?
source: https://firebase.blog/posts/2025/06/app-hosting-frameworks/
author: firebase.blog
published: '2025-06-02T00:00:00Z'
fetched: '2025-06-05T23:43:55Z'
tags:
- codex
- firebase
- hosting
- javascript
- frameworks
- serverless
image: https://firebasestorage.googleapis.com/v0/b/first-class-blog.appspot.com/o/og%2Fapp-hosting-frameworks.png?alt=media&token=8bb19a16-a705-4164-aa36-3ab2f0420eb7
---

## 要約

Firebase App Hosting は、Angular と Next.js を中心に GA となったサーバレス型の Web ホスティングです。公式サポート以外にも、**Nitro** ベースのアダプターを利用することで **Nuxt** や **Tanstack Start**、**SolidStart**、**Analog** など多くのフレームワークがデプロイ可能です。さらに **Astro**、**SvelteKit**、**Vite** などもビルド成果物が仕様を満たせば利用でき、Firebase CLI もしくは Terraform を用いたコンテナデプロイも選択できます。設定例として `firebase.json` の記述が紹介され、フレームワーク開発者向けにアダプター実装のガイドラインも提示されています。

## 本文

June 2, 2025

Firebase App Hosting, a serverless web hosting service built for modern, full-stack web apps, [recently graduated to General Availability](https://firebase.blog/posts/2025/04/apphosting-general-availability) with headline support for Angular and Next.js. However, there are a lot more JavaScript frameworks out there. Can we deploy them to App Hosting?

**Note:** This post focuses on frameworks that are compatible with [the App Hosting build process](https://firebase.google.com/docs/app-hosting/build), where App Hosting automatically builds and deploys your web app either from a push to git or from the Firebase CLI. Alternatively, you can build containers yourself and use [App Hosting’s Terraform support](https://firebase.google.com/docs/projects/terraform/get-started#resources-app-hosting) to deploy to an App Hosting backend. Building the containers yourself means you could deploy any web server with any language, like .NET, Go, or Python. That’s a topic for another blog post, though.

### Angular and Next.js

First, a quick recap: App Hosting has [pre-configured build and deploy support for Angular and Next.js web apps](https://firebase.google.com/docs/app-hosting/frameworks-tooling#frameworks-with-preconfigured-build-and-deploy-support). These are maintained by the App Hosting team, and have a documented [support schedule](https://firebase.google.com/docs/app-hosting/frameworks-tooling#next.js-support).

When you use a supported version of either framework, App Hosting builds and deploys your web app without any extra work required. There are also [docs for supported package managers and monorepo tooling](https://firebase.google.com/docs/app-hosting/frameworks-tooling#package-managers).

In addition to built-in Angular and Next.js support, App Hosting [documents the expected output of a build system](https://firebase.google.com/docs/app-hosting/frameworks-tooling#community-supported-frameworks) so that any framework can create an adapter to deploy to App Hosting. The full list of community adapters is available at [firebaseopensource.com](https://firebaseopensource.com/platform/app_hosting).

#### Nitro: Analog, Nuxt, SolidStart, Tanstack Start

[Nitro](https://nitro.build/deploy/providers/firebase) is the server toolkit that powers SSR functionality for lots of frameworks. We’ve collaborated with the Nitro team on a community adapter to make App Hosting a [Zero-Config Provider](https://nitro.build/deploy#zero-config-providers), which means that [Nuxt](https://nuxt.com/deploy/firebase), [Tanstack Start](https://tanstack.com/start/latest), [SolidStart](https://start.solidjs.com/), and [Analog](https://analogjs.org/) will all work without any extra configuration.

#### Astro

We also have a [proof-of-concept community adapter for Astro](https://github.com/FirebaseExtended/firebase-framework-tools/pull/297) in the works. To use it, first install the adapter:

$npx astro add @apphosting/astro-adapter

Then, update your Astro config file to reference the adapter:

astro.config.mjs

```
import { defineConfig } from 'astro/config';
import node from '@apphosting/astro-adapter';

export default defineConfig({
  output: 'server',
  adapter: node({
      mode: 'standalone',
  }),
});
```

#### A note for framework authors

App Hosting looks for a `.apphosting/bundle.yaml` file that lets you tell App Hosting what commands should be used for build and run, where your framework’s build artifacts are, and what specific Cloud Run settings are needed to run your framework. That way, developers using your framework don’t need to do any extra work to deploy their web apps. As we add features to App Hosting, adapters will get more valuable.

If you’re a framework author curious about the [output bundle spec](https://github.com/FirebaseExtended/firebase-framework-tools?tab=readme-ov-file#app-hosting-output-bundle), here’s a sample:

Sample `.apphosting/bundle.yaml` file

.apphosting/bundle.yaml

```
version: v1
runConfig:
  runCommand: node dist/index.js
  environmentVariables:
      - variable: VAR
        value: 8080
        availability: RUNTIME
  concurrency: 80
  cpu: 2
  memoryMiB: 512
  minInstances: 0
  maxInstances: 14

outputFiles:
  serverApp:
      include:
          - dist
          - .output

metadata:
  adapterPackageName: npm-name
  adapterVersion: 12.0.0
  framework: framework-name
  frameworkVersion: 1.0.0
```

### …any framework?

Here’s the thing. When App Hosting doesn’t recognize your framework, it falls back to the Node.js [Cloud buildpack](https://cloud.google.com/docs/buildpacks/overview), which knows how to build all kinds of Node projects. That means that, even without a specific adapter, your app can work on App Hosting.

> Most JavaScript frameworks will work on App Hosting with minimal extra configuration.

#### The Node.js buildpack

The Node.js buildpack takes the following steps to build and run your app:

In Cloud Build, the buildpack checks your `package.json` for a `build` or `apphosting:build` script. Some kind of build script is required - if not, the build will fail.

In Cloud Run, the buildpack tries quite a few things to start the server for your web app. If you have any of the following, you’ll be able to deploy your app on App Hosting:

1. A SvelteKit app.
2. A `start` script in `package.json`.
3. A `server.js` file in the root of your project.
4. A `main` field in `package.json` pointing to your server code.
5. An `index.js` file in the root of your project.

The buildpack actually tries even more than this, but the above is most
relevant to App Hosting. You can view the buildpack source
code for [build](https://github.com/GoogleCloudPlatform/buildpacks/blob/17165a4156e95e2e9eb55ab631190d2d042e9954/pkg/nodejs/npm.go#L150) and [run](https://github.com/GoogleCloudPlatform/buildpacks/blob/17165a4156e95e2e9eb55ab631190d2d042e9954/pkg/nodejs/npm.go#L212)
if you’re curious.

You’ll also need to modify your server code to [listen on the correct port](https://cloud.google.com/run/docs/container-contract#port) with the `PORT` environment variable that is automatically injected.

Let’s see how these rules let us deploy different frameworks:

#### SvelteKit

[SvelteKit](https://svelte.dev/docs/kit/introduction) is supported by the Node.js buildpack with no extra configuration.

#### React Router with SSR (Remix)

Following the standard [React Router quickstart](https://reactrouter.com/start/framework/installation) is all you need to do, since that includes a `build` script as well as a `start` script with a built-in production server:

$npx create-react-router@latest

#### Express

[Express](https://expressjs.com/) is still a popular way to host static websites or API servers. As long as there is an npm `build` and `start` script, we’re set. Here’s an example for a “hello world” Express server:

server.mjs

```
import express from "express";

const app = express();

const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
```

package.json

```
{
  "name": "express-on-apphosting",
  "version": "1.0.0",
  "description": "A basic Express server on Firebase App Hosting",
  "main": "server.mjs",
  "scripts": {
      "build": "echo \"no-op build script\"",
      "start": "node server.mjs"
  },
  "dependencies": {
      "express": "^5.1.0"
  }
}
```

Note the build script that just prints “no-op build script” - there needs to
be something there for a successful App Hosting build. If you wrote your server with TypeScript, you could run your TypeScript build here.

#### Hono

The default [Hono](https://hono.dev/) Node.js template has a `build` and `run` command, which is a great start.

$npm create hono@latest --template nodejs

The only thing we need to modify is the port that the server listens on:

src/index.ts

```
import { serve } from "@hono/node-server";
import { Hono } from "hono";

const app = new Hono();

app.get("/", (c) => {
  return c.text("Hello Hono!");
});

serve({
  fetch: app.fetch,

  port: process.env.PORT ? parseInt(process.env.PORT) : 8080
},
  (info) => {
      console.log(`Server is running on http://localhost:${info.port}`);
  },
);
```

#### Caveats for relying on the Node.js buildpack

The main difference between using frameworks that don’t have an official or community adapter is that adapters may have specific tuning of Cloud Run instances to best suit the framework, or special environment variables that enhance framework functionality.

Instead, you can set these yourself:

### Static web apps (SPAs)

[We still recommend the original Firebase Hosting for static web apps](https://firebase.blog/posts/2024/05/app-hosting-vs-hosting). However, if you’d like to deploy a static web app to App Hosting, you certainly can with the help of a static server like [superstatic](https://www.npmjs.com/package/superstatic) or [serve](https://www.npmjs.com/package/serve) to run in your App Hosting backend. It takes two steps in the command line:

```
npm install superstatic




npm pkg set scripts.start="superstatic <your folder here> --port \$PORT --host 0.0.0.0"

```

#### React SPA with Vite

Here’s an example of a static single-page app (SPA) built with React, TypeScript, and Vite from the `react-ts` Vite template:

```
npm create vite@latest react-spa -- --template react-ts
cd react-spa
npm install superstatic
npm pkg set scripts.start="superstatic dist --port \$PORT --host 0.0.0.0"

```

Running these commands will result in this `package.json` file:

react-spa/package.json

```
{
  "name": "react-spa",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
      "dev": "vite",
      "build": "tsc && vite build",
      "start": "superstatic dist --port $PORT --host 0.0.0.0"
  },
  "devDependencies": {
      "typescript": "~5.7.2",
      "vite": "^6.3.2",
      "@types/react": "^19.1.2",
      "@types/react-dom": "^19.1.2"
  },
  "dependencies": {
      "react": "^19.1.0",
      "react-dom": "^19.1.0",
      "superstatic": "^9.2.0"
  }
}
```

Since there is a `build` script and a `run` script, App Hosting will be able to deploy and serve your static React app.

#### Cache static content

Static content won’t change until your next rollout, so it is worth heavily [caching content in Cloud CDN](https://firebase.google.com/docs/app-hosting/optimize-cache). Most static file servers should have settings for this.

In the case of superstatic, create a `superstatic.json` config file and reference it from your `start` script:

```
npm pkg set scripts.start="superstatic dist --port \$PORT --host 0.0.0.0 -c superstatic.json"

```

This example caches content for an hour (3600 seconds):

react-spa/superstatic.json

```
{
  "headers": [
      {
          "source": "**",
          "headers": [
              {
                  "key": "Cache-Control",
                  "value": "public, max-age=3600"
              }
          ]
      }
  ]
}
```

It’s fine to set long cache timeouts because the CDN tags will be purged on every new rollout.

### Use your favorite framework on App Hosting

While Angular and Next.js are the best-supported frameworks for App Hosting, we hope it’s clear that it’s ready for nearly any JavaScript-powered web app you’d like to build. If you’re a framework maintainer, you can make it even easier for developers to deploy to App Hosting by [following the output bundle specification](#a-note-for-framework-authors).

If you haven’t already, head over to the [Firebase console](http://console.firebase.google.com/project/_/apphosting) and explore our [documentation](http://firebase.google.com/docs/app-hosting) to deploy your first app. As always, if you have questions, you can hit us up on any of our [support channels](https://firebase.google.com/support).

And if you have ideas for any new features, let us know on [User Voice](https://firebase.uservoice.com/forums/948424-general?category_id=501599). Your feedback matters and will help us continue to make App Hosting the best web hosting platform for you.
