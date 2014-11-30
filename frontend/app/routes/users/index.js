import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    console.log("This is the user route.");
    return this.store.find('user');
  },
});
