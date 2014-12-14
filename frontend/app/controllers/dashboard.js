import Ember from 'ember';

export default Ember.Controller.extend({
  datafiles: Ember.computed.mapBy('datasets', 'names'),
  classifier_files: Ember.computed.mapBy('classifiers', 'names'),
  actions: {
    submit: function() {
      alert("Form submitted with the following files!");
    }
  }
});
