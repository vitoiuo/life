<template>
  <div id="app">
      <h1 style='text-align: center'>Life Game</h1>
      <lifeVue />
  </div>
</template>

<script>
import lifeVue from './components/lifeVue.vue'

export default {
  name: 'App',
  components: {
    lifeVue
  }
}
</script>
