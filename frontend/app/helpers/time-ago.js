import Ember from 'ember';

export function timeAgo(input) {
  console.log("Doing formatting.");
  console.log(input);
  return moment(input).fromNow();
}

export default Ember.Handlebars.makeBoundHelper(timeAgo);
