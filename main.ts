// News-image entry for 23 November 2026: ship the entry.png beside this
// file to the output directory. The image sums up the day in six stories:
// Huang's return to Nvidia, the Merkury sinking off Libya, the Grok
// lawsuits, Iran's blockade vow, Puigdemont's return, and the cobalt halt.
// Node 22, standard library only; the grader sets MAKEFUN_OUTPUT_DIR
// outside its container, /output is the default.
import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = new URL('./entry.png', import.meta.url);
if (!existsSync(source)) {
  throw new Error('entry.png is missing from the repository');
}
mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, 'entry.png'));
