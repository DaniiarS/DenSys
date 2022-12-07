<template>
  <input type="text"
         :value="search"
         @input="event => Searched(event, input)"
         class="max-w-full relative border-0 mx-4 px-4 py-3 placeholder-slate-300 text-slate-600 bg-white rounded text-sm shadow focus:outline-none focus:ring ease-linear transition-all duration-150"
         placeholder="Search"/>
</template>
<script>

export default {

  model: {
    prop: 'output',
    event: 'update:output'
  },

  props: ['input', 'output'],
  data() {
    return {
      search:null,
    };
  },
  methods: {
    FilterArray(search, arr) {
      var matches = []
      if (!Array.isArray(arr) || arr.length == 0) {
        return matches
      }
      matches = arr.filter((obj) => {
        if (typeof obj === "string" || obj instanceof String) {
          if (obj.toLowerCase().includes(this.search.toLowerCase())) {
            return true
          }
        }
        else if (obj instanceof Date) {
          console.log(obj.toString())
          if (obj.toString().toLowerCase().includes(this.search.toLowerCase())) {
            return true
          }
        }
        else if (typeof obj === 'object' && obj !== null) {
          let res = this.FilterArray(this.search, Object.values(obj))
          if (res.length) {
            return true
          }
        }
      })
      return matches
    },
    Searched(e) {
      this.search = e.target.value
      var matches = []
      matches = this.input.filter((obj) => {
        if (typeof obj === "string" || obj instanceof String) {
          if (obj.toLowerCase().includes(this.search.toLowerCase())) {
            return true
          }
        }
        else if (obj instanceof Date) {
          console.log(obj.toString())
          if (obj.toString().toLowerCase().includes(this.search.toLowerCase())) {
            return true
          }
        }
        else if (typeof obj === 'object' && obj !== null) {
          let res = this.FilterArray(this.search, Object.values(obj))
          if (res.length) {
            return true
          }
        }
      })

      console.log("matches: ", matches)
      this.$emit('update:output', matches)
    }
  },
  mounted () {
  }
};
</script>
