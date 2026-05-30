/**
 * VNN Service Worker
 * Handles push notifications for Valyrian News Network
 */

self.addEventListener('push', (event) => {
  console.log('Push event received:', event);
  
  let data = {};
  if (event.data) {
    try {
      data = event.data.json();
      console.log('Push data:', data);
    } catch (e) {
      console.log('Push data (text):', event.data.text());
      // Try to show a generic notification if JSON parsing fails
      data = { title: 'New Article', body: 'Check VNN for updates' };
    }
  } else {
    console.log('Push event has no data');
    data = { title: 'New Article', body: 'Check VNN for updates' };
  }
    
  const options = {
    body: data.body || '',
    icon: data.icon || '/favicon.svg',
    badge: data.badge || '/favicon.svg',
    data: {
      url: data.url || '/',
    },
    tag: 'vnn-article',
    renotify: true,
  };

  event.waitUntil(
    self.registration.showNotification(data.title || 'Valyrian News Network', options)
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  const url = event.notification.data?.url || '/';

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      // Check if there's already a window open
      for (const client of clientList) {
        if (client.url.includes('valyriantech.github.io/ValyrianNewsNetwork') && 'focus' in client) {
          client.navigate(url);
          return client.focus();
        }
      }
      // Open new window if none exists
      if (clients.openWindow) {
        return clients.openWindow(url);
      }
    })
  );
});

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(clients.claim());
});
