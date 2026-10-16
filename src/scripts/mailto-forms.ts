/**
 * GitHub Pages can't receive form posts, so forms marked with data-subject open the
 * visitor's email app with a pre-filled message to the organisation instead.
 */
import { CONTACT } from '../data/site';

export function initMailtoForms(root: ParentNode = document): void {
  root.querySelectorAll<HTMLFormElement>('form[data-subject]').forEach((form) => {
    if (form.dataset.bound) return;
    form.dataset.bound = 'true';
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const lines: string[] = [];
      form.querySelectorAll<HTMLInputElement | HTMLTextAreaElement>('input, textarea').forEach((field) => {
        if (field.value.trim()) lines.push(`${field.placeholder || field.name}: ${field.value.trim()}`);
      });
      const subject = encodeURIComponent(form.dataset.subject ?? 'Website message');
      const body = encodeURIComponent(lines.join('\n'));
      window.location.href = `mailto:${CONTACT.email}?subject=${subject}&body=${body}`;
    });
  });
}
