<script setup>
import { RouterView } from 'vue-router'
import AppHeader from './components/AppHeader.vue'
import AppSidebar from './components/AppSidebar.vue'
</script>

<template>
  <AppHeader title="MrMat :: Python API :: FastAPI"/>
  <main>
    <aside>
      <AppSidebar/>
    </aside>
    <div>
      <RouterView/>
    </div>
  </main>
</template>

<style>
@import './assets/base.css';

main {
  display: flex;
  flex: 1;
  flex-direction: row;
}

main > aside {
  height: 100%;
}

main > aside > div {
  height: 100%;
}

main > div {
  margin: 14px 10px 0 14px;
}
</style>
