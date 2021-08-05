<template>
  <div>    
    <router-view />
    <footer-rodape />
  </div>
</template>
<script>
/*import HeaderNavbar from "./components/template/HeaderNavbar.vue";*/
import FooterRodape from "./components/template/FooterRodape.vue";

export default {
  components: { FooterRodape },
};
</script>
<style>
</style>
