<template>
  <nav class="left-0 block fixed top-0 bottom-0 overflow-y-auto flex-row flex-nowrap overflow-hidden shadow-xl bg-white flex items-center justify-between w-64 z-10 py-4 px-6">
    <div class="flex-col items-stretch min-h-full flex-nowrap px-0 justify-between w-full mx-auto" >
      <div>
      <!-- Toggler -->
      <button class="inline-block cursor-pointer text-black opacity-50 px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
              type="button">
        <i class="fas fa-bars"></i>
      </button>
      <!-- Brand -->
      <router-link class="inline-block text-left text-slate-600 text-sm uppercase font-bold
                          mr-0 pb-2 p-4 px-0
                          whitespace-nowrap"
                   to="/">
        {{header}}
      </router-link>
      </div>
      <!-- Collapse -->
      <div class="flex flex-col items-stretch opacity-100 relative mt-4 shadow-none absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-auto h-auto items-center flex-1 rounded">
        <!-- Divider -->
        <hr class="my-4 min-w-full" />
        <!-- Heading -->
        <h6 class="min-w-full text-slate-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline">
          {{subheader}}
        </h6>
        <!-- Navigation -->

        <ul class="flex-col min-w-full flex flex-col list-none">
          <li class="items-center" v-for="(btn, bidx) in buttons" :key="bidx">
            <router-link :to="btn.link"
                         v-slot="{ href, navigate, isActive, }">
              <a :href="href"
                 @click="if (btn.click) {btn.click()}; navigate"
                 class="text-xs uppercase py-3 font-bold block"
                :class="[
                  isActive
                    ? 'text-emerald-500 hover:text-emerald-600'
                    : 'text-slate-700 hover:text-slate-500']">
                <i class="mr-2 text-sm fa-2x fa-fw"
                   :class="[isActive ? 'opacity-75' : 'text-slate-300', btn.icon]" >
                </i>
                {{btn.name}}
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
  props: {
    buttons: {
      type: Array,
      default: () => [{
        name: 'Name',
        link: '/admin',
        click: '',
        icon: 'fas fa-user',
      },
      ]
    },
    header: {
      type: String,
      default: 'header'
    },
    subheader: {
      type: String,
      default: 'subheader'
    },
  },

  data() {
    return {
    };
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token')
    },
  },
  components: {
    //NotificationDropdown,
    //UserDropdown,
  },
};
</script>
