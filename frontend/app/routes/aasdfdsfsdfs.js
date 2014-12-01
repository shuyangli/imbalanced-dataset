import Ember from 'ember';
import User from "../models/user";

export default Ember.Route.extend({
  model: function() {
    console.log("This is the user route.");
    //console.log(User.find());
    return this.store.find('user');
  },
});
