<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p></p>
  </div>
</template>

<script>
import {get} from '../utils/http'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      data: []
    }
  },
  created() {
   get('http://172.16.5.54:5050/api/test').then(data=>{
     console.log(data)
   }) 
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
