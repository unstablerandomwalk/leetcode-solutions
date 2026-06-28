class MinStack {
    private int[] stack;
    private int[] minStack;
    private int size;
    public MinStack() {
        stack = new int[16];
        minStack = new int[16];
        size = 0;
    }
    public void push(int value) {
        if (size == stack.length) {
            stack = java.util.Arrays.copyOf(stack, size * 2);
            minStack = java.util.Arrays.copyOf(minStack, size * 2);
        }
        stack[size] = value;
        minStack[size] = (size == 0) ? value : Math.min(value, minStack[size - 1]);
        size++;
    }

    public void pop() {
        size--;
    }

    public int top() {
        return stack[size - 1];
    }

    public int getMin() {
        return minStack[size - 1];
    }
}