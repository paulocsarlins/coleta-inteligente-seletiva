<template>
  <div>
    <list-companies></list-companies>
  </div>
</template>

<script>
import ListCompanies from './components/companies/ListCompanies.vue'

export default {
  name: 'App',
  components: {
    ListCompanies
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
