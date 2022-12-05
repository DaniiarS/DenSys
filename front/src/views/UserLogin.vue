<template>
  <div
    class="flex bg-slate-100 m-auto items-center justify-center w-screen h-screen"
  >
    <div class="w-full lg:w-4/12 shadow-lg rounded-lg bg-slate-200 border-0">
      <div class="px-4 lg:px-10 py-10 pt-0">
        <div class="text-slate-800 text-center py-3 font-bold">Login</div>
        <form>
          <div class="relative w-full mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              IIN
            </label>
            <input
              type="text"
              v-model="iin"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              placeholder="IIN"
            />
          </div>
          <div class="relative w-full mb-3">
            <label
              class="block uppercase text-slate-600 text-xs font-bold mb-2"
            >
              Password
            </label>
            <input
              type="password"
              v-model="password"
              class="border-0 px-3 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
              placeholder="Password"
            />
          </div>

          <div class="text-center mt-6">
            <button
              class="bg-slate-800 text-white active:bg-slate-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
              type="button"
              @click="Submit"
            >
              Sign In
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { server_url } from "@/api.js";

export default {
  data() {
    return {
      password: "",
      iin: "",
    };
  },
  methods: {
    Submit() {
      axios
        .post(server_url + "/api/token/", {
          username: this.iin,
          password: this.password,
        })
        .then((response) => {
          console.log(response.data);
          localStorage.setItem("access_token", response.data.token);
          localStorage.setItem("user_iin", response.data.user_iin);
          localStorage.setItem("who", response.data.who);
          axios.defaults.headers.common[
            "Authorization"
          ] = `Token ${localStorage.getItem("access_token")}`;
          console.log(response.data.who);
          if (response.data.who === "patient") {
            this.$router.push({ path: "/patient" });
          } else if (response.data.who === "doctor") {
            this.$router.push({ path: "/doctor" });
          } else if (response.data.who === "admin")
            this.$router.push({ path: "/admin" });
        })
        .catch(function (error) {
          alert("Fail");
          console.log(error);
        });
    },
  },
};
</script>
