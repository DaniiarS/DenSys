<template>
  <div>
  <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-slate-200">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
      Hello
      {{iin}}
    </div>
  </div>
  </div>
</template>
<script>
import axios from 'axios'
import {server_url} from '@/api.js'

export default {
  data() {
    return {
      iin:'',
    };
  },
  methods: {
    Submit() {
      axios
        .post(server_url + '/api/token/', {
          username: this.iin,
          password: this.password
        })
        .then(response => {
          console.log(response.data)
          localStorage.setItem('access_token', response.data.token)
          localStorage.setItem('user_iin',     response.data.user_iin)
          axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('access_token')}`;
          if (response.data.who === "patient") {
            this.$router.push({path: '/patient'})
          } else if (response.data.who === 'doctor') {
            this.$router.push({path: '/doctor'})
          }
        })
        .catch(function (error) {
          alert("Fail")
          console.log(error)
        })
    },
  },
  mounted() {
    this.iin = localStorage.getItem('user_iin')
  }
};
</script>
