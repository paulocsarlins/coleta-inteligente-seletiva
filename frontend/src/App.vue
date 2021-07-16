<template>
  <div>
    <pontos-de-coleta></pontos-de-coleta>
  </div>
</template>

<script>
import PontosDeColeta from './components/template/PontosDeColeta.vue'

export default {
  name: 'App',
  components: {
    PontosDeColeta
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
