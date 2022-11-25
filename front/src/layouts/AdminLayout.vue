<template>
  <div>
    <sidebar />
    <div class="relative ml-64 bg-slate-100 py-10 min-h-screen">
      <div class="px-4 mb-10 md:px-10 mx-auto w-full">
        <router-view />
      </div>
      <footer-admin />
    </div>
  </div>
</template>
<script>

//import AdminNavbar from "@/components/Navbars/AdminNavbar.vue"
import Sidebar from "@/components/SidebarComponent.vue"
import FooterAdmin from "@/components/FooterAdmin.vue"
//import HeaderStats from "@/components/Headers/HeaderStats.vue"

export default {
  name: "admin-layout",
  components: {
    //AdminNavbar,
    Sidebar,
    FooterAdmin,
   // HeaderStats,
  },
  mounted () {
    if (!localStorage.access_token) {
      this.$router.push({path: '/admin/login'})
    }
    console.log(localStorage.access_token)
  }
};
</script>
