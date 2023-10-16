import java.util.Random;

public class NameGenerator {
    private static final String[] prefixes = {"John", "Emma", "Michael", "Olivia", "William", "Ava", "James", "Sophia"};
    private static final String[] suffixes = {"Smith", "Johnson", "Brown", "Lee", "Davis", "Evans", "Garcia", "Hill"};

    public static void main(String[] args) {
        Random random = new Random();

        // Generate a random name
        String generatedName = generateRandomName(random);
        System.out.println("Generated Name: " + generatedName);
    }
//thats the code

    private static String generateRandomName(Random random) {
        // Randomly select prefix and suffix
        String randomPrefix = prefixes[random.nextInt(prefixes.length)];
        String randomSuffix = suffixes[random.nextInt(suffixes.length)];

        // Combine prefix and suffix to form the name
        return randomPrefix + " " + randomSuffix;
    }
}
In this code, the NameGenerator class contains two arrays: prefixes and suffixes, which store common first names and last names, respectively. The generateRandomName method uses the Random class to select a random prefix and a random suffix, then combines them to create a random name.

Please note that this example is very basic and does not guarantee unique or realistic names. For more realistic results, you might want to consider using larger datasets of names. Also, consider handling edge cases or adding additional complexity based on your specific requirements.





