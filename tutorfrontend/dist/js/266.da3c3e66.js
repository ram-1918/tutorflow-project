"use strict";(self["webpackChunktutorfrontend"]=self["webpackChunktutorfrontend"]||[]).push([[266],{266:function(e,s,t){t.r(s),t.d(s,{default:function(){return U}});var r=t(3396),a=t(9242),l=t(7139);const n=e=>((0,r.dD)("data-v-570a24fe"),e=e(),(0,r.Cn)(),e),i={id:"id01",class:"modal"},d=n((()=>(0,r._)("span",{class:"register-title"},"Register",-1))),u=n((()=>(0,r._)("br",null,null,-1))),o={key:0,class:"error-msg"},p={key:1,class:"error-msg"},m={key:2,class:"error-msg"},w=n((()=>(0,r._)("br",null,null,-1))),c={class:"container"},h=n((()=>(0,r._)("legend",null,"Firstname",-1))),f=n((()=>(0,r._)("legend",null,"Lastname",-1))),_=n((()=>(0,r._)("legend",null,"Email",-1))),g=n((()=>(0,r._)("legend",null,"Password",-1))),k=n((()=>(0,r._)("legend",null,"Re-enter Password",-1)));function y(e,s,t,n,y,E){const b=(0,r.up)("base-header"),v=(0,r.up)("base-button"),U=(0,r.up)("router-link");return(0,r.wg)(),(0,r.iD)(r.HY,null,[(0,r.Wm)(b),(0,r._)("div",i,[(0,r._)("form",{class:"modal-content",onSubmit:s[5]||(s[5]=(0,a.iM)((e=>E.register()),["prevent"]))},[d,u,this.$store.state.err?((0,r.wg)(),(0,r.iD)("span",o,(0,l.zw)(this.$store.state.err),1)):(0,r.kq)("",!0),y.passErr?((0,r.wg)(),(0,r.iD)("span",p,(0,l.zw)(y.passErr),1)):(0,r.kq)("",!0),y.emailErr?((0,r.wg)(),(0,r.iD)("span",m,(0,l.zw)(y.emailErr),1)):(0,r.kq)("",!0),w,(0,r._)("div",c,[(0,r._)("fieldset",null,[h,(0,r.wy)((0,r._)("input",{type:"text",placeholder:"","onUpdate:modelValue":s[0]||(s[0]=e=>y.firstname=e),required:""},null,512),[[a.nr,y.firstname]])]),(0,r._)("fieldset",null,[f,(0,r.wy)((0,r._)("input",{type:"text",placeholder:"","onUpdate:modelValue":s[1]||(s[1]=e=>y.lastname=e),required:""},null,512),[[a.nr,y.lastname]])]),(0,r._)("fieldset",null,[_,(0,r.wy)((0,r._)("input",{type:"text",placeholder:"","onUpdate:modelValue":s[2]||(s[2]=e=>y.email=e),required:""},null,512),[[a.nr,y.email]])]),(0,r._)("fieldset",null,[g,(0,r.wy)((0,r._)("input",{type:"password",placeholder:"","onUpdate:modelValue":s[3]||(s[3]=e=>y.psw1=e),required:""},null,512),[[a.nr,y.psw1]])]),(0,r._)("fieldset",null,[k,(0,r.wy)((0,r._)("input",{type:"password",placeholder:"","onUpdate:modelValue":s[4]||(s[4]=e=>y.psw2=e),required:""},null,512),[[a.nr,y.psw2]])]),(0,r.Wm)(v,{type:"submit",mode:"submit"},{default:(0,r.w5)((()=>[(0,r.Uk)("SignUp")])),_:1}),(0,r.Uk)(" or SignIn using "),(0,r.Wm)(U,{to:"/login"},{default:(0,r.w5)((()=>[(0,r.Uk)("SignIn")])),_:1})])],32)])],64)}var E={data(){return{firstname:"",lastname:"",email:"",phone:"",psw1:"",psw2:"",passErr:"",emailErr:""}},methods:{register(){var e=/^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/,s=/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;if(this.email=this.email.trim().toLowerCase(),s.test(this.email))if(this.psw1===this.psw2)if(e.test(this.psw1)){var t={firstname:this.firstname.trim().toLowerCase(),lastname:this.lastname.trim().toLowerCase(),email:this.email,password:this.psw1};this.$store.dispatch("register",{data:t})}else this.passErr="Password should include lower and upper case charecters, a special charecter, and a number.";else this.passErr="Passwords Didn't match!";else this.emailErr="Enter a valid Email address!"}}},b=t(89);const v=(0,b.Z)(E,[["render",y],["__scopeId","data-v-570a24fe"]]);var U=v}}]);
//# sourceMappingURL=266.da3c3e66.js.map