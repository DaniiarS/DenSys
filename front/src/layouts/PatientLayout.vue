<template>
  <div>
    <sidebar
      :header="'DenSys Patient'"
      :subheader="'Patient Actions'"
      :buttons="[
                 {name: 'Profile',          icon: 'fas fa-id-card',            link: '/patient/profile'},
                 {name: 'Services',         icon: 'fas fa-kit-medical',        link: '/patient/service-request'},
                 {name: 'Make Appointment', icon: 'fas fa-calendar-plus',      link: '/patient/make-appointment'},
                 {name: 'Requests',         icon: 'fas fa-clipboard-list',     link: '/patient/requests'},
                 {name: 'Patient History',  icon: 'fas fa-book-medical',       link: '/patient/history'},
                 {name: 'Logout',           icon: 'fas fa-right-from-bracket', link: '/', click:logout},
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
  name: "admin-layout",
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
    if (localStorage.who != 'patient') {
      this.$router.push({ path: "/" });
    }
    console.log(localStorage.access_token);
  },
  methods: {
    logout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("user_iin");
      localStorage.removeItem("who");
    },
  },
};
</script>
