/**
 * GitHub Pages can't receive form posts, so forms marked with data-subject open the
 * visitor's email app with a pre-filled message to the organisation instead.
 * The browser's built-in validation runs first, so required fields are announced
 * to screen readers before anything happens.
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
        const label = form.querySelector(`label[for="${field.id}"]`)?.textContent?.replace(/\*|\(required\)/g, '').trim();
        if (field.value.trim()) lines.push(`${label || field.name}: ${field.value.trim()}`);
      });
      const subject = encodeURIComponent(form.dataset.subject ?? 'Website message');
      const body = encodeURIComponent(lines.join('\n'));
      window.location.href = `mailto:${CONTACT.email}?subject=${subject}&body=${body}`;
    });
  });
}
