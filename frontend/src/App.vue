<template>
  <ul>
    <li v-for="user of users" v-bind:key="user">
      {{user.name}} - {{user.email}}
    </li>
  </ul>
</template>

<script>
import axios from 'axios'


export default {
  name: 'App',
  data(){
    return {
      users: []

    }
  },
  created: function(){
    
    /*axios.post('http://localhost:8000/registration/', {'username': '', 'password1': '', 'password2': ''})
      .then(result => console.log(result))
        .error(error => console.log(error));
    */
    
    axios.get('http://localhost:8000/api/users')
      .then(result => {
        this.users = result.data;
      }).catch(error => {
        console.log(error);
      }) 
  }
}
</script>

<style>

</style>
