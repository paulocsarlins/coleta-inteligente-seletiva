<template>
  <div>
    <lista-denuncias></lista-denuncias>
  </div>
</template>

<script>
import ListaDenuncias from './components/denuncias/ListaDenuncias.vue'

export default {
  name: 'App',
  components: {
    ListaDenuncias
  },
  data(){
    return {
      users: []

    }
  },
  created: function(){
    
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,400;0,700;1,100&display=swap');

html, body {
  font-family: 'Poppins', sans-serif;
}

body {
  zoom: 0.9;
}
</style>
