const fs = require('fs');
let css = fs.readFileSync('src/styles/swiss.css', 'utf8');

// Fix the corrupted top comment
css = css.replace(/\* All rules are wrapped in so they ONLY/g, '* All rules are wrapped in [data-theme-name="swiss"] so they ONLY');

// Fix the missing selector on line 35
css = css.replace(/\n{\n/g, '\n[data-theme-name="swiss"],\n[data-theme-name="default"],\n[data-theme-name="default-large"] {\n');

// Wrap all top-level selectors (not starting with space or @ or [data-theme-name)
const lines = css.split('\n');
let inRule = false;
let inComment = false;
let inAtRule = false;

for (let i = 0; i < lines.length; i++) {
  let line = lines[i];
  
  if (line.includes('/*')) inComment = true;
  if (line.includes('*/')) { inComment = false; continue; }
  if (inComment) continue;

  if (line.startsWith('@')) {
    if (!line.includes('{') && line.endsWith(';')) continue;
    inAtRule = true;
  }
  
  // If it's a selector line (doesn't start with space, isn't empty, doesn't start with @ or }, or [data-theme-name)
  if (line.length > 0 && !line.startsWith(' ') && !line.startsWith('}') && !line.startsWith('@') && !line.startsWith('[data-theme-name') && !inRule && !inAtRule) {
    // Check if it's actually a selector (ends with , or { on same line or next lines)
    if (line.includes('{') || line.endsWith(',')) {
      lines[i] = ':is([data-theme-name="swiss"], [data-theme-name="default"], [data-theme-name="default-large"]) ' + line;
    }
  }

  if (line.includes('{')) {
    inRule = true;
  }
  if (line.includes('}')) {
    inRule = false;
    inAtRule = false;
  }
}

fs.writeFileSync('src/styles/swiss.css', lines.join('\n'));
console.log('Fixed swiss.css');
