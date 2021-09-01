<template>
    <div class="container mt-2">
        <h1 class="mb-3">Add new data:</h1>
        <form @submit.prevent="onSubmit">
            <div class="row">
                <div class="col">
                <input 
                    v-model="editor_date"
                    type="text" 
                    class="form-control"
                    placeholder="Date">
                </div>
                <div class="col">
                <input
                    v-model="editor_distance"
                    type="text" 
                    class="form-control" 
                    placeholder="Distance">
                </div>
                <div class="col">
                <input 
                    v-model="editor_duration"
                    type="text" 
                    class="form-control" 
                    placeholder="Duration">
                </div>
            </div>
                <div class="my-2">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"
export default {
    name: "UserEditor",
    data() {
        return {
            
            editor_date: null,
            editor_distance: null,
            editor_duration: null,
            editor_user: "admin@localhost",
            error: null
        }
    },
    methods: {
        onSubmit() {
            if(!this.editor_date) {
                this.error = "you can't send an empty data" ;
            } else {
                let endpoint = "api/speed/";
                let method = "POST";
                apiService(endpoint, method, {content: this.editor_body})
                    .then(editor_data => {
                        this.$router.push({ 
                            name: 'add-data',
                            params: { slug: editor_data.slug }   })
                })
            }
        }
    
    },
    created() {
        document.title = "Editor - Report Page";
    }
}
</script>