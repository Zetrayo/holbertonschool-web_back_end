import { taskFirst, getLast, taskNext } from './yourFile.js';

test('taskFirst returns correct string', () => {
  expect(taskFirst()).toBe('I prefer const when I can.');
});

test('getLast returns correct string', () => {
  expect(getLast()).toBe(' is okay');
});

test('taskNext combines task and last correctly', () => {
  expect(taskNext()).toBe('But sometimes let is okay');
});
