<template>
  <div id="app">
    <Header></Header>
    <router-view id="router-view" :key="$route.fullPath"/>
  </div>
</template>

<script>
import Header from './components/Header'
export default {
  name: 'App',
  components: {Header}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#router-view {
  margin-top: 2%;
  padding-left: 0;
  padding-right: 0;
}
</style>
