<template>
  <footer class="block py-4 md:flex md:items-center">
    <div class="container mx-auto px-4">
      <hr class="mb-4 border-b-1 border-slate-200" />
      <div
        class="flex flex-wrap items-center md:justify-between justify-center"
      >
        <div class="w-full md:w-4/12 px-4">
          <div
            class="text-sm text-slate-500 font-semibold py-1 text-center md:text-left"
          >
            Copyright © {{ date }}
            <a
              href="/"
              class="text-slate-500 hover:text-slate-700 text-sm font-semibold py-1"
            >
              DenSys
            </a>
          </div>
        </div>
        <div class="w-full md:w-8/12 px-4">
          <ul class="flex flex-wrap list-none md:justify-end justify-center">
            <li>
              <a
                href="/contactus"
                class="text-slate-600 hover:text-slate-800 text-sm font-semibold block py-1 px-3"
              >
                Contact Us
              </a>
            </li>
            <li>
              <a
                href="/aboutus"
                class="text-slate-600 hover:text-slate-800 text-sm font-semibold block py-1 px-3"
              >
                About Us
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      date: new Date().getFullYear(),
    };
  },
};
</script>
