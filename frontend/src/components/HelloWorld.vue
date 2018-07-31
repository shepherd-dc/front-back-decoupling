<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p></p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  created() {
   this.$http.get('http://www.kanyanbao.com/newsadapter2/autonews_speak.json?id=917827').then(data=>{
     console.log(data)
   }) 
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
