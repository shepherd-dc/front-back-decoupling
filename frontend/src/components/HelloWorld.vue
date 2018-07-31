<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p v-for="item in tasks">{{item.title}}</p>
  </div>
</template>

<script>
import { SERVER_URI } from '../../global.js'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      tasks: []
    }
  },
  created() {
   this.$http.get(SERVER_URI+'/api/test').then(data=>{
    //  console.log(data.data)
     this.tasks = data.data.tasks
   })
   this.$http.get(SERVER_URI+`/api/test/${this.msg}`).then(data=>{
     console.log(data)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
