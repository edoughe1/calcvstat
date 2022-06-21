def get_recommend(course, major):
  if course == "Algebra 2" and major == "Business" or "Social Studies and the Humanities":
    return "Statistics"
  elif course == "Algebra 2" and major == "Science, Technology, Engineering, or Math" or "Natural Sciences":
    return "Pre-Calculus"
  elif course == "Pre-Calculus" and major == "Science, Technology, Engineering, or Math" or "Natural Sciences":
    return "Calculus"
  elif course == "Pre-Calculus" and major == "Business" or "Social Studies and the Humanities":
    return "Statistics"
  else:
    return "Please try again"