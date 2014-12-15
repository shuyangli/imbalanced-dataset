import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {

  },

  setupController: function(controller, model) {
     this._super(controller,model);
     controller.set('datasets', this.store.find('dataset'));
     controller.set('classifiers', this.store.find('classifier'));
     controller.set('users', this.store.find('user'));
     controller.set('analyses', this.store.find('analysis'));
     controller.set('test_outputs', this.store.find('test_output'));
  }
});
