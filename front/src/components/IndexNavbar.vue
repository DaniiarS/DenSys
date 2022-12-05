<template>
  <nav
    class="top-0 fixed z-50 w-full flex flex-wrap items-center justify-between px-2 py-3 navbar-expand-lg bg-white shadow"
  >
    <div
      class="container px-4 mx-auto flex flex-wrap items-center justify-between"
    >
      <div
        class="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start"
      >
        <router-link to="/">
          <a
            class="text-blueGray-700 text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase"
          >
            Den Sys
          </a>
        </router-link>
        <button
          class="cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
          type="button"
          v-on:click="setNavbarOpen"
        >
          <i class="fas fa-bars"></i>
        </button>
      </div>
      <div
        class="lg:flex flex-grow items-center"
        :class="[navbarOpen ? 'block' : 'hidden']"
        id="example-navbar-warning"
      >
        <ul class="flex flex-col lg:flex-row list-none mr-auto">
          <li class="flex items-center">
            <button
              @click="selectButton('make-appointment')"
              class="active:bg-emerald-600 text-xs font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150"
              :class="
                selected == 'make-appointment'
                  ? 'bg-slate-200 text-emerald-500'
                  : 'bg-emerald-500 text-white'
              "
              type="button"
            >
              Make Appointment
            </button>
            <button
              @click="selectButton('service-request')"
              class="active:bg-emerald-600 text-xs font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150"
              :class="
                selected == 'service-request'
                  ? 'bg-slate-200 text-emerald-500'
                  : 'bg-emerald-500 text-white'
              "
              type="button"
            >
              Service Request
            </button>
          </li>
        </ul>
        <ul class="flex flex-col lg:flex-row list-none lg:ml-auto">
          <!-- <li class="flex items-center">
            <index-dropdown />
          </li> -->
          <li v-if="!logged" class="flex items-center">
            <button
              @click="this.$router.push({ path: '/login' })"
              class="bg-emerald-500 text-white active:bg-emerald-600 text-xs font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150"
              type="button"
            >
              Login
            </button>
          </li>
          <li v-if="logged" class="flex items-center">
            <button
              @click="this.$router.push({ path: '/' + logged })"
              class="bg-emerald-500 text-white active:bg-emerald-600 text-xs font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150"
              type="button"
            >
              {{ logged + " Profile" }}
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
// import IndexDropdown from "@/components/Dropdowns/IndexDropdown.vue";

export default {
  data() {
    return {
      logged: "",
      navbarOpen: false,
      selected: "",
    };
  },
  methods: {
    setNavbarOpen: function () {
      this.navbarOpen = !this.navbarOpen;
    },
    selectButton: function (name) {
      this.selected = name;
      this.$router.push({ path: "/" + name });
    },
  },
  mounted() {
    this.logged = localStorage.getItem("who");
  },
  components: {
    // IndexDropdown,
  },
};
</script>
