<template>
  <div>
    <sidebar
      :header="'DenSys Patient'"
      :subheader="'Patient Actions'"
      :buttons="[
        { name: 'Profile', icon: 'fas fa-id-card', link: '/doctor/profile' },
        {
          name: 'My Appointments',
          icon: 'fas fa-clipboard-list',
          link: '/doctor/my-appointment',
        },
        {
          name: 'My Patients',
          icon: 'fas fa-clipboard-list',
          link: '/doctor/my-patients',
        },
        {
          name: 'Logout',
          icon: 'fas fa-right-from-bracket',
          link: '/login',
          click: logout,
        },
      ]"
    />
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
import Sidebar from "@/components/SidebarComponent.vue";
import FooterAdmin from "@/components/FooterMain.vue";
//import HeaderStats from "@/components/Headers/HeaderStats.vue"

export default {
  components: {
    //AdminNavbar,
    Sidebar,
    FooterAdmin,
    // HeaderStats,
  },
  mounted() {
    if (!localStorage.access_token) {
      this.$router.push({ path: "/login" });
    }
    console.log(localStorage.access_token);
  },
  methods: {
    logout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("user_iin");
    },
  },
};
</script>
