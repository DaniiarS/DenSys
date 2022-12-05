<template>
  <div class="relative">
    <index-navbar />
    <div class="pt-24">
      <router-view />
    </div>
  </div>
  <footer-main />
</template>

<script>
import IndexNavbar from "@/components/IndexNavbar.vue";
import FooterMain from "@/components/FooterMain.vue";
export default {
  data() {
    return {};
  },
  components: {
    IndexNavbar,
    FooterMain,
  },
};
</script>
