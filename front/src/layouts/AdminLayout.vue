<template>
  <div>
    <sidebar
    :header="'DenSys Admin'"
    :subheader="'Admin Actions'"
    :buttons="[ {name: 'Patient Registration', icon: 'fas fa-clipboard-user',     link: '/admin/patient-register'},
                {name: 'Doctor Registration',  icon: 'fas fa-stethoscope',        link: '/admin/doctor-register'},
                {name: 'Service Registration', icon: 'fas fa-square-plus',        link: '/admin/service-register'},
                {name: 'Patients',             icon: 'fas fa-user',               link: '/admin/patients'},
                {name: 'Doctors',              icon: 'fas fa-user-doctor',        link: '/admin/doctors'},
                {name: 'Services',             icon: 'fas fa-kit-medical',        link: '/admin/service'},
                {name: 'Requests',             icon: 'fas fa-clipboard-list',     link: '/admin/requests'},
                {name: 'Logout',               icon: 'fas fa-right-from-bracket', link: '/admin/login', click:logout},
              ]"
    />
    <div class="relative ml-64 bg-slate-100 py-10 min-h-screen">
      <div class="px-4 mb-10 md:px-10 mx-auto w-full">
        <router-view />
      </div>
    </div>
  </div>
</template>
<script>
//import AdminNavbar from "@/components/Navbars/AdminNavbar.vue"
import Sidebar from "@/components/SidebarComponent.vue";
//import HeaderStats from "@/components/Headers/HeaderStats.vue"

export default {
  name: "admin-layout",
  components: {
    //AdminNavbar,
    Sidebar,
    // HeaderStats,
  },
  mounted() {
    if (!localStorage.access_token) {
      this.$router.push({ path: "/admin/login" });
    } else if (localStorage.who !== 'admin') {
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
