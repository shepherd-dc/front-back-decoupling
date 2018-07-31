<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p v-for="item in tasks">{{item.title}}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      tasks: []
    }
  },
  created() {
   this.$http.get('http://172.16.5.54:5050/api/test').then(data=>{
     console.log(data.data)
     this.tasks = data.data.tasks
   }) 
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
