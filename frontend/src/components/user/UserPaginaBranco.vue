<template>
  <div>
    <user-header-navbar />
    <h1 class="title1">🚧 Página em desenvolvimento! 🚧</h1> 
    <div class="container1">
        
      <div class="c-loader"></div>
    </div>
  </div>
</template>

<script>
import UserHeaderNavbar from "./UserHeaderNavbar.vue";
export default {
  components: { UserHeaderNavbar },
  name: "home",
  data() {
    return {};
  },
};
</script>

<style>
.container1 {
  margin-top: 5%;
  margin-left: 38%;
}
.title1 {
  text-align: center;
  font-size: 3rem;
  font-weight: bold;
  text-shadow: 0.0em 0.0em 0.2em black;
}
.c-loader {
  animation: is-rotating 1s infinite;
  border: 6px solid #e5e5e5;
  border-radius: 50%;
  border-top-color: #3d9e42;
  height: 400px;
  width: 400px;
}

@keyframes is-rotating {
  to {
    transform: rotate(1turn);
  }
}
</style>
