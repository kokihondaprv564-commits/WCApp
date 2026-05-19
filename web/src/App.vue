<template>
  <div>
    <header class="app-header">
      <div class="brand">WCApp</div>
    </header>
    <main class="app-main">
      <router-view />
    </main>
  </div>
</template>

<style>
body { font-family: system-ui, sans-serif; margin: 0; }
.app-header { position: sticky; top: 0; background: #0f172a; color: white; padding: 0.6rem 1rem; z-index:20 }
.brand { font-weight:700 }
.app-main { padding: 1rem }
</style>
