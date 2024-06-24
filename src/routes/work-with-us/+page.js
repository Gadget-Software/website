import fs from 'fs';

import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/** @type {import('./$types').PageLoad} */
export function load({ params }) {
  return {
    copyHtml: fs.readFileSync(__dirname + '/copy.html'),
  };
}
