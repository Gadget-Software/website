import { publish } from 'gh-pages';

publish(
  'build',
  {
    branch: 'gh-pages',
    repo: 'https://github.com/sofutoka/gadget-software-website.git',
    user: {
      name: 'Eduardo Lavaque',
      email: 'me@greduan.com',
    },
    dotfiles: true,
  },
  () => {
    console.log('Deploy Complete!');
  },
);
