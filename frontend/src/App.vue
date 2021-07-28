<template>
<div>
     <header-navbar></header-navbar>
     <router-view />
</div>
</template>
<script>

import HeaderNavbar from "./components/template/HeaderNavbar.vue";

export default {
  components: { HeaderNavbar }
}
</script>
<style>
</style>
