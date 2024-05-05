<template>
    <div class="footer" id="about">
        <div class="col-2" :style="{width: this.$store.state.isMobile ? '80%':'30%'}">
            <div class="row-1">
                <span id="title">TutorFlow</span><br>
                <span id="about">TutorFlow is a dynamic blog created and designed to provide an interactive platform for users to create their own study space. With TutorFlow, users can connect and engage with like-minded individuals to share knowledge, exchange ideas and collaborate on study projects.</span>
            </div>
            <div class="row-2">
                <span id="sub-title">Developed & Designed by - RCB</span>
            </div>
        </div>
        <div class="col-1" :style="{width: this.$store.state.isMobile ? '100%':'30%'}">
            <h2>Contact Details</h2>
            <div class="contact-table">
                    <table>
                        <tr>
                            <td id="heading"><i class="fa fa-home" style="font-size:18px"></i></td>
                            <td>Edison, NJ, 08817, USA</td>
                        </tr>
                        <tr>
                            <td id="heading"><i class="fa fa-envelope" style="font-size:18px"></i></td>
                            <td>ramchandra0426@gmail.com</td>
                        </tr>
                        <tr>
                            <td id="heading"><i class="fa fa-phone" style="font-size:18px"></i></td>
                            <td>+1 (732) 474-8217</td>
                        </tr>
                        <tr>
                            <td id="heading"><i class="fa fa-linkedin" style="font-size:18px"></i></td>
                            <td><a :href='linkedin' target="_blank">Linkedin</a></td>
                        </tr>
                        <tr>
                            <td id="heading"><i class="fa fa-github" style="font-size:18px"></i></td>
                            <td><a :href='github' target="_blank">GitHub</a></td>
                        </tr>
                    </table>
                </div>
        </div>

        <div class="col-3" :style="{width: this.$store.state.isMobile ? '100%':'30%'}">
            <h2>Please leave a feedback!</h2>
            <!-- <div class="feedback-form"> -->
            <form @submit.prevent="submitFeedback" class="col-3-form">
                <input type="email" v-model="email" placeholder="Enter your email..." v-if="!this.$store.state.currUser.isLoggedIn">
                <textarea rows="3" v-model="feedback" placeholder="Enter your Feedback..."></textarea>
                <base-button mode="feedback-submit">Submit</base-button>
            </form>
            <!-- </div> -->
        </div>

    </div>
</template>
<script>

export default {
    data(){
        return {
            email: '',
            feedback: '',
            linkedin: 'https://www.linkedin.com/in/ramchandrab2604/',
            github: 'https://github.com/ram-1918'
        }
    },
    methods:{
        submitFeedback(){
            const payload = {
                "email": this.$store.state.currUser.isLoggedIn ? this.$store.state.currUser.data.user.email : this.email,
                "feedback": this.feedback
            }
            this.$store.dispatch('postFeedback', payload);
            this.email = ''
            this.feedback = ''
        }
    }
   };
</script>
<style scoped>
.footer{
    bottom:0;
    left: 0;
    position: relative;
    width: 100%;
    /* height: 15rem; */
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    background-color: #302c36; /*#19171D;*/
    color:#D1D2D3;
}
.col-1{
    /* width: 30%; */
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;

}
.col-2{
    width:40%;
    display: flex;
    flex-direction: column;
    background-color: inherit;
}
.col-3{
    /* width: 30%; */
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

}
.contact-table{
    font-size: medium;
}
.contact-table table{
    text-align: center;
    margin:auto;
}
.contact-table table td{
    padding: 5px;
    float: left;
    font-size: 0.9rem;
}
#heading{
    font-weight: bolder;
    font-size: 1rem;
}
#title{
    font-size: 1.8rem;
    font-family: cursive;
    font-weight: bolder;
}
#sub-title{
    font-size: 0.7rem;
    font-family:Arial, Helvetica, sans-serif;
}
#about{
    font-size: 0.8rem;
    font-weight: 200;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.row-1{
    width:100%;
    text-align:center;
    margin: auto;
}

.row-2{
    width: 100%;
    text-align: center;
}
.col-3-form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 200px;
}
.col-3 textarea{
    max-width: 90%;
    min-width: 70%;
    max-height: 55%;
    min-height: 55%;
    font-size: medium;
    border: none;
}
.col-3 textarea:focus{
    outline: none;
}
textarea::placeholder{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: small;
}
input[type=email]{
    padding: 8px;
    width: 70%;
    border: none;
    margin: 10px;
    /* background-color: inherit;
    border-bottom: 1px solid #D1D2D3;
    color: #D1D2D3; */
}
input[type=email]:focus{
    outline: none;
}

a{
    text-decoration: none;
    color: inherit;
}

@media screen and (max-width: 600px){
    .footer{
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        background-color: #1a5998;
    }
    .col-1, .col-2, .col-3{
        width: 100%;
    }
    h2{
        margin-top: 2rem;
        margin-bottom: 0;
        font-size: 1.2rem;
    }
}

</style>