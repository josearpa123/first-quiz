package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  private static VendingMachineImpl instance;
  private int insertedMoney;

  private VendingMachineImpl() {
    insertedMoney = 0;
  }

  public static VendingMachine getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    insertedMoney += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if ("ScottCola".equals(name)) {
      if (insertedMoney >= 75) {
        insertedMoney = 0; // Reset the money for the next transaction
        return new Drink() {
          @Override
          public String getName() {
            return "ScottCola";
          }

          @Override
          public boolean isFizzy() {
            return true;
          }
        };
      } else {
        throw new NotEnoughMoneyException();
      }
    } else if ("KarenTea".equals(name)) {
      if (insertedMoney >= 100) {
        insertedMoney = 0; // Reset the money for the next transaction
        return new Drink() {
          @Override
          public String getName() {
            return "KarenTea";
          }

          @Override
          public boolean isFizzy() {
            return false;
          }
        };
      } else {
        throw new NotEnoughMoneyException();
      }
    } else {
      throw new UnknownDrinkException();
    }
  }
}
