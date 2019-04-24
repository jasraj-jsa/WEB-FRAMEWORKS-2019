<template>
    <div class='home1'>
        <img src="./profile.png" v-bind:style="profile"> 
    </div>
</template>

<script>
export default{
    data(){
        return{
            profile: {
                top: '-50px',
                width: '100px',
                height: '100px',
                borderRadius: '50%',
                position: 'absolute',
                left: 'calc(50% - 50px)',
            }
        }
    }
}

</script>
<style type='text/css' scoped>

</style>