<template lang="html">

    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listas Hola!!</h2>

                <div class="col-md-12">
                    <b-table striped hover :items="users" :fields="fields"> 

                    </b-table>
                </div>

            </div>
        </div>
    </div>   

</template>

<script>
export default {
    data(){
        return{
            fields: [
                { key: 'nombre', label: 'Nombre'},
                { key: 'apellido', label: 'Apellido'},
                { key: 'area', label: 'area'}
            ],
            users:[]
        }
                
    }
    
}
</script>

<style lang="css" scoped>

</style>

