<template>
  <!--
 shadow-xl bg-white items-center justify-between relative z-10 py-4 px-6 w-64 left-0 block fixed top-0 bottom-0 overflow-y-auto flex-row flex-nowrap overflow-hidden
  -->

  <nav class="left-0 block fixed top-0 bottom-0 overflow-y-auto flex-row flex-nowrap overflow-hidden shadow-xl bg-white flex items-center justify-between w-64 z-10 py-4 px-6">
    <div class="flex-col items-stretch min-h-full flex-nowrap px-0 justify-between w-full mx-auto" >
      <div>
      <!-- Toggler -->
      <button class="inline-block cursor-pointer text-black opacity-50 px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
              type="button"
              v-on:click="toggleCollapseShow('')">
        <i class="fas fa-bars"></i>
      </button>
      <!-- Brand -->
      <router-link class="inline-block text-left text-slate-600 text-sm uppercase font-bold
                          mr-0 pb-2 p-4 px-0
                          whitespace-nowrap"
                   to="/">
        Hello
      </router-link>
      </div>
      <!-- Collapse -->
      <div class="flex flex-col items-stretch opacity-100 relative mt-4 shadow-none absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-auto h-auto items-center flex-1 rounded"
           v-bind:class="collapseShow">
        <!-- Divider -->
        <hr class="my-4 min-w-full" />
        <!-- Heading -->
        <h6 class="min-w-full text-slate-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline">
          Admin Actions
        </h6>
        <!-- Navigation -->

        <ul class="flex-col min-w-full flex flex-col list-none">
          <li class="items-center">
            <router-link to="/admin/patient-register"
                         v-slot="{ href, navigate, isActive, }">
              <a :href="href"
                 @click="navigate"
                 class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-700 hover:text-blueGray-500']">
                <i class="fas fa-clipboard-user mr-2 text-sm fa-2x fa-fw"
                   :class="[isActive ? 'opacity-75' : 'text-blueGray-300']" >
                </i>
                Patient Registration
              </a>
            </router-link>
          </li>
          <li class="items-center">
            <router-link to="/admin/doctor-register"
                         v-slot="{ href, navigate, isActive, }">
              <a :href="href"
                 @click="navigate"
                 class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-700 hover:text-slate-500']">
                <i class="fas fa-stethoscope mr-2 text-sm fa-fw fa-2x"
                   :class="[isActive ? 'opacity-75' : 'text-slate-300']" >
                </i>
                Doctor Registration
              </a>
            </router-link>
          </li>
          <li class="items-center">
            <router-link to="/admin/patients"
                         v-slot="{ href, navigate, isActive, }">
              <a :href="href"
                 @click="navigate"
                 class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-700 hover:text-blueGray-500']">
                <i class="fas fa-user mr-2 text-sm fa-2x fa-fw"
                   :class="[isActive ? 'opacity-75' : 'text-blueGray-300']" >
                </i>
                Patients
              </a>
            </router-link>
          </li>
          <li class="items-center">
            <router-link to="/admin/doctors"
                         v-slot="{ href, navigate, isActive, }">
              <a :href="href"
                 @click="navigate"
                 class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-700 hover:text-blueGray-500']">
                <i class="fas fa-user-doctor mr-2 text-sm fa-2x fa-fw"
                   :class="[isActive ? 'opacity-75' : 'text-blueGray-300']" >
                </i>
                Doctors
              </a>
            </router-link>
          </li>
          <li class="items-center">
            <router-link
              to="/admin/dashboard"
              v-slot="{ href, navigate, isActive }"
            >
              <a
                :href="href"
                @click="navigate"
                class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-700 hover:text-blueGray-500',
                ]"
              >
                <i
                  class="fas fa-tv mr-2 text-sm fa-2x fa-fw"
                  :class="[isActive ? 'opacity-75' : 'text-blueGray-300']"
                ></i>
                Dashboard
              </a>
            </router-link>
          </li>

          <li class="items-center">
            <router-link
              to="/admin/settings"
              v-slot="{ href, navigate, isActive }"
            >
              <a
                :href="href"
                @click="navigate"
                class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-700 hover:text-blueGray-500',
                ]"
              >
                <i
                  class="fas fa-tools mr-2 text-sm fa-2x fa-fw"
                  :class="[isActive ? 'opacity-75' : 'text-blueGray-300']"
                ></i>
                Settings
              </a>
            </router-link>
          </li>

          <li class="items-center">
            <router-link to="/admin/tables"
                         v-slot="{ href, navigate, isActive }" >
              <a :href="href"
                @click="navigate"
                class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-blueGray-700 hover:text-blueGray-500',
                ]">
                <i class="fas fa-table mr-2 text-sm fa-2x fa-fw"
                   :class="[isActive ? 'opacity-75' : 'text-blueGray-300']" >
                </i>
                Tables
              </a>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
); }

<script>
//import NotificationDropdown from "@/components/Dropdowns/NotificationDropdown.vue";
//import UserDropdown from "@/components/Dropdowns/UserDropdown.vue";

export default {

  data() {
    return {
      collapseShow: "active",
    };
  },
  methods: {
    toggleCollapseShow: function (classes) {
      this.collapseShow = classes;
    },
  },
  components: {
    //NotificationDropdown,
    //UserDropdown,
  },
};
</script>
